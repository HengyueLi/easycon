# easycon  
A easy-use tool to connect to a remote server, by which one can easily login, upload and download files to and from a remote server. One can also connect to a server behind a NAT. This tool is developed on `paramiko`. 
## Install  
`pip install easycon` 
## Usage 
One can find the instruction by run command `easycon` in terminal directly.  
(For windows users, one can try `easycon` or `easycon.bat`)

In the following, some of the examples are given:

* login remote server:  
`easycon --config <configfile> --login`  
(One can obtain a `<configfile>` template by `--mkconfig` )  
* upload file(dir) into remote server:  
`easycon --config <configfile> --put <example.txt>`  
* download file(dir) from server:  
`easycon --config <configfile> --get <example.txt>`  
* jump over NAT:  
scenery: One need to login a server that is in a private subnet (behind a NAT) shown as following:  
`local host` --> `jumpbox` --> `target` 
One can get two configurate file `<jump.txt>` and `<target.txt>` and execute:  
`easycon --config <target.txt> --jump <jump.txt>`  

One can find more in instruction.


 

## Update 

### 2019.03.31
add --jump

### 2019.03.27
add --loginw

### 2019.03.16
Update sshapi.  

### Update 2019.03.10 
Windows supported

### Update 2019.03.08  
1. fix bug  
  Fix know bugs for login. This is an old issue relate to stdin. Details see [here](https://github.com/paramiko/paramiko/issues/302). The solution is [here](https://github.com/rogerhil/paramiko/commit/4c7911a98acc751846e248191082f408126c7e8e). 
2. add `put`/`get` to upload/download directory  
3. change the format of the configuration file.
