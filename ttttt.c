#include<stdio.h>
#include<pthread.h>
void* task3(void* arg)
{
	int i;
	for(i=0;i<5;i++)
	{
		printf("Task 3 running...\n");
	}
	return NULL;
}
void* task4(void* arg)
{
	int i;
	for(i=0;i<4;i++)
	{
		printf("Task 4 running...\n");
	}
	return NULL;
    }
int main()
{
	pthread_t t3,t4;
	pthread_create(&t3,NULL,task4,NULL);
	pthread_create(&t4,NULL,task3,NULL);
	pthread_join(t3,NULL);
	pthread_join(t4,NULL);
	return 0;
}
