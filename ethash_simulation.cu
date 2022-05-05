#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <cuda_runtime.h>
using namespace std;
#define group_size 8
#define dag_size 1024*1024*1024

#if (__CUDACC_VER_MAJOR__ > 8)
#define SHFL(x, y, z) __shfl_sync(0xFFFFFFFF, (x), (y), (z))
#else
#define SHFL(x, y, z) __shfl((x), (y), (z))
#endif

#define FNV_PRIME 0x01000193
#define fnv(x, y) ((x)*FNV_PRIME ^ (y))

__global__ void test_dag_device(int *dag, int nonce, int *result_device) {
    int tix = threadIdx.x;
    int tiy = threadIdx.y;
    int bix = blockIdx.x;
    int biy = blockIdx.y;
    int bdx = blockDim.x;
    int bdy = blockDim.y;
    int gdx = gridDim.x;
    int gdy = gridDim.y;
    int thread_id = bdx * bix + tix;

    int start_nonce[8];
    int end_nonce[8];

    for(int i=0;i<=7;i++){
        start_nonce[i]= nonce + i + thread_id;
    }

    const int thread_id_ingroup = threadIdx.x & (group_size - 1);
    const int mix_idx = thread_id_ingroup & 3;
    

    for(int i=0;i<=group_size-1;i++){

        int mix;
        int init;
        int offset;
        int shuffle[8];

        for(int j=0;j<=7;j++){
            shuffle[j] = SHFL(start_nonce[j], i, group_size);
        }

        switch(mix_idx){
            case 0:
                mix = shuffle[0] + shuffle[1];
                break;
            case 1:
                mix = shuffle[2] + shuffle[3];
                break;
            case 2:
                mix = shuffle[4] + shuffle[5];
                break;
            case 3:
                mix = shuffle[6] + shuffle[7];
                break;
        }

        init = SHFL(shuffle[0], 0, group_size);

        for(int k =0;k<=63;k++){
            offset = fnv(init ^ k, mix)%dag_size;
            offset = SHFL(offset, k%8, group_size);
            mix = fnv(mix, dag[offset]&thread_id_ingroup);
        }

        int shuffle2[8];
        int thread_mix = mix;
        shuffle2[0] = SHFL(thread_mix, 0, group_size);
        shuffle2[1] = SHFL(thread_mix, 1, group_size);
        shuffle2[2] = SHFL(thread_mix, 2, group_size);
        shuffle2[3] = SHFL(thread_mix, 3, group_size);
        shuffle2[4] = SHFL(thread_mix, 4, group_size);
        shuffle2[5] = SHFL(thread_mix, 5, group_size);
        shuffle2[6] = SHFL(thread_mix, 6, group_size);
        shuffle2[7] = SHFL(thread_mix, 7, group_size);

        if(i==thread_id_ingroup){
            end_nonce[0] = shuffle2[0];
            end_nonce[1] = shuffle2[1];
            end_nonce[2] = shuffle2[2];
            end_nonce[3] = shuffle2[3];
            end_nonce[4] = shuffle2[4];
            end_nonce[5] = shuffle2[5];
            end_nonce[6] = shuffle2[6];
            end_nonce[7] = shuffle2[7];
        }
    }
    int sum=0;
    for(int i=0;i<=7;i++){
        sum = sum+end_nonce[i];
    }
    result_device[thread_id%1024] = sum;
}

int main()
{
    double size = dag_size;
    int *dag_host;
    int *dag_device;
    int *result_host;
    int *result_device;

    cout<<"start"<<endl;
    int nonce = 1010;
    dag_host = (int*) malloc(sizeof(int) * size);

    srand(0);

    for(int i=0;i<=size-1;i++){
        if((int)rand()/RAND_MAX > 0.5){
            dag_host[i]=-1;
        }
        else{
            dag_host[i]=1;
        }
    }

    cudaMalloc((void**)&dag_device,sizeof(int) *size);
    cudaMalloc((void**)&result_device,sizeof(int) *1024);

    cudaMemcpy(dag_device,dag_host,sizeof(int) *size,cudaMemcpyHostToDevice);

    dim3 gridsize(8192,1,1);
    dim3 blocksize(128,1,1);

    cout<<"Dag generate finished!"<<endl;

    int count = 0;
    while(1){
        test_dag_device<<<gridsize,blocksize>>>(dag_device, nonce, result_device);
        count = count + 1;

        if(count % 10000 == 0)
            cout<<"Hash finished "<<count<<" times!"<<endl;
    }

    // cudaMemcpy(result_host, result_device,sizeof(int) *size,cudaMemcpyDeviceToHost);

    // cudaFree(dag_device);
    // cudaFree(result_device);



}