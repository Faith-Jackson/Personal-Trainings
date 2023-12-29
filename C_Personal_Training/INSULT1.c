#include <stdio.h>
#include <string.h>

int main() {
	    char jerk[20];
	        
		    printf("Name some jerk you know: ");
		        fgets(jerk, sizeof(jerk), stdin);

			    // Remove trailing newline character if present
			        jerk[strcspn(jerk, "\n")] = '\0';

				    printf("Yeah, I think %s is a jerk, too.\n", jerk);
				        return 0;
}

