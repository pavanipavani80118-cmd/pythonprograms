#include<stdio.h>
#include<pthread.h>
void* task1(void* arg)
{
	int i;
	for(i=0;i<5;i++)
	{
	printf("Task1 running...\n");
	}
	return  NULL;
	}
	void* task2(void* arg)
	{
	int i;
	for(i=0;i<4;i++)
	{
	printf("Task2 running...\n");
	}
	return NULL;
	}

	{
		int i;
		for(i=0;i<3;i++)
		printf("Task 3 running...\n");		
	}
	return NULL;
	}
	int main()
  {
	pthread_t t1,t2,t3;
	pthread_create(&t1,NULL,task1,NULL,);
	pthread_create(&t2,NULL,task2,NULL);
pthread_join(t1,NULL);
	pthread_join(t2,NULL);
    return 0;
	}
	
