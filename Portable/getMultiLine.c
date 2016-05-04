#include<stdio.h>

/**
@status built, not completely tested
Cpl doesn't support default parameter value? (or C99 that gcc uses?)
So getMultiLine(char*) is the lite version of getMultiLinePro(char*,int)...
*/
int getMultiLine(char* s){
	int start=0,end=0; // start and end of in loop

	for(start=0,end=0;;++end){
		s[end]=getchar();

		if(s[end]=='\n'){ // a line ends
			if(end==start){ // a lonely \n indicates the end of input
				s[end-1]='\0'; // s[end] is the lonely \n, s[end-1] is \n of the last line
				return end-1;
			}
			else{ // simply start a new line
				start=end+1;
			}
		}
	}
}

/**
@status building
For char s[100], should call getMultiLine_s(s,100).
Of course, maximum 99 chars can be read. Last char reserve for '\0'.

When exceeding ( overflowing? whatever ) happends, cut it and return -1.

考虑 截断在不同位置.
maxlen=5
123\n\n
1234\n
12345\n
*/
int getMultiLine_s(char* s,int maxlen){
	int start=0,end=0; // start and end of in loop
	char ch='#';

	for(start=0,end=0;end<maxlen+1;++end){
		if((ch=getchar())=='\n'){ // a line ends
			if(end==start){ // a lonely \n indicates the end of input
				s[end-1]='\0'; // s[end] is the lonely \n, s[end-1] is \n of the last line
				return end-1;
			}
			else{ // simply start a new line
				start=end+1;
			}
		}
	}
	setbuf(stdin, NULL); // win, linux available

}


/**
@status built, not completely tested

@param:
s: The char pointer identifying the string, should be <dynamically / statically> malloced

@function:
Input multiline.
Input a line with a only "Enter", then input will end.

@return: 
The length of s, \n(or/and \r) included.

@todo lineend or newline characters differ in varios Operating system... ONLY tested in Windows
*/
#define DONT_RESTORE_LAST_NEWLINE_CHAR 0
#define RESTORE_LAST_NEWLINE_CHAR 1
int getMultiLinePro(char* s,int OPTION_restore_last_newline_char){
	int start=0,end=0; // start and end of in loop
	
	for(start=0,end=0;;++end){
		s[end]=getchar();

		if(s[end]=='\n'){ // a line ends
			if(end==start){ // a lonely \n indicates the end of input
				if(OPTION_restore_last_newline_char){ 
					s[end]='\0'; // s[end] is the lonely \n, s[end-1] is \n of the last line
					return end;
				}
				else{
					s[end-1]='\0'; // s[end] is the lonely \n, s[end-1] is \n of the last line
					return end-1;
				}
			}
			else{ // simply start a new line
				start=end+1;
			}
		}
	}
}

int main(){
	char ss[1024];
	int len=getMultiLine(ss);
	printf("=========\n");
	// printf("%d\n", len);
	// printf("%d\n", strlen(ss));
	printf("%s\n", ss);
	printf("=========\n");
}
