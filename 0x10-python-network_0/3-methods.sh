#!/bin/bash
#this will show the list of possible methods a url can accept
curl -sL -i $1 | grep -i "Allow:" |cut -d ' ' -f2-
<<<<<<< HEAD

=======
>>>>>>> f8c731af94b140db6c896fa3ef55e78bb97a7d02
