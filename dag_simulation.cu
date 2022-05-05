#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <cuda_runtime.h>
using namespace std;


__global__ void test_dag_device(float *dag, float nonce, float *result_device) {
    int tix = threadIdx.x;
    int tiy = threadIdx.y;
    int bix = blockIdx.x;
    int biy = blockIdx.y;
    int bdx = blockDim.x;
    int bdy = blockDim.y;
    int gdx = gridDim.x;
    int gdy = gridDim.y;
    int thread_id = bdx * bix + tix;
    float start_nonce = nonce + float(thread_id);

    for(int i =0;i<=63;i++){
        start_nonce = start_nonce + dag[thread_id];
    }

    result_device[thread_id%1024] = start_nonce;
}

int main()
{
    double size = 1024*1024*1024;
    float *dag_host;
    float *dag_device;
    float *result_host;
    float *result_device;

    cout<<"start"<<endl;
    float nonce = 1010;
    dag_host = (float*) malloc(sizeof(float) * size);
    srand(0);
    for(int i=0;i<=size-1;i++){
        if((float)rand()/RAND_MAX > 0.5){
            dag_host[i]=-1;
        }
        else{
            dag_host[i]=1;
        }
    }

    cudaMalloc((void**)&dag_device,sizeof(float) *size);
    cudaMalloc((void**)&result_device,sizeof(float) *1024);

    cudaMemcpy(dag_device,dag_host,sizeof(float) *size,cudaMemcpyHostToDevice);


    dim3 gridsize(8192,1,1);
    dim3 blocksize(128,1,1);

    while(1){
        test_dag_device<<<gridsize,blocksize>>>(dag_device, nonce, result_device);
    }

    cudaMemcpy(result_host, result_device,sizeof(float) *size,cudaMemcpyDeviceToHost);

    cudaFree(dag_device);
    cudaFree(result_device);



}