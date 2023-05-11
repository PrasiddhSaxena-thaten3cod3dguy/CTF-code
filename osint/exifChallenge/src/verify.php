<?php
    if(isset($_POST['login']))
    {
        $response['username']="alpha";
    $response['success']=true;
    $user = $_POST['username'];
    $pass = $_POST['password'];
    $htmldata = "<div>
    <pre>
    9183  docker build -t stegano
    9184  docker build
    9185  docker build Dockerfile
    9186  docker build --help
    9187  docker built -t
    9188  clear
    9189  ls
    9190  docker build
    9191  cat Dockerfile
    9192  code Dockerfile
    9193  docker build ./
    9194  docker run -p 20:20 c158a2e8eec9
    9195  systemctl
    9196  docker image ls
    9197  docker image rm c158a2e8eec9
    9198  docker image rm -rf c158a2e8eec9
    9199  docker image rm --help
    9200  docker image rm -f c158a2e8eec9
    9201  docker image ls
    9202  clear
    9203  whois 192.168.43.1
    9204  nslookup 127.0.0.1
    9205  dig 127.0.0.1
    9206  hackdev
    9207  ctf
    9208  ftpStegano
    9209  ls
    9210  cat Dockerfile
    9211  code Dockerfile
    9212  hackdev/ctf/archive/
    9213  ls
    9214  apache
    9215  ls
    9216  apache
    9217  ls
    9218  cat Dockerfile
    9219  systemctl status vsftpd
    9220  docker build ./
    9221  docker run 785a4a215791 -d -it
    9222  docker run 785a4a215791
    9223  docker image
    9224  docker image ls
    9225  docker rmi 785a4a215791
    9226  docker rmi -f 785a4a215791
    9227  docker image ls
    9228  docker build -t ctf
    9229  docker build ./
    9230  docker run 23dbde2b8753
    9231  ls
    9232  cat vsftpd.conf
    9233  ftp 192.168.43.16
    9234  clear
    9235  ls
    9236  ../
    9237  ../../
    9238  ftpStegano
    9239  ls
    9240  rm vsftpd.*
    9241  ls
    9242  mv ../archive/apache/apache/vsftpd.c* ./
    9243  ls
    9244  docker image ls
    9245  docker rmi 23dbde2b8753
    9246  docker rmi -f 23dbde2b8753
    9247  clear
    9248  docker build ./
    9249  docker run b661fbaf0ab1
    9250  clear
    9251  docker image ls
    9252  docker rmi b661fbaf0ab1
    9253  docker rmi -f b661fbaf0ab1
    9254  ../
    9255  archive/apache/apache
    9256  clear
    9257  ls
    9258  docker build ./
    9259  ../archive/apache/apache
    9260  ls
    9261  code .
    9262  docker image ls
    9263  docker rmi -f b568e77e9de4
    9264  claer
    9265  clear
    9266  code sample.html
    9267  ls
    9268  hackdev/ctf/ftpStegano
    9269  ls
    9270  nano vsftpd
    9271  ls
    9272  code Dockerfile
    9273  ls
    9274  docker build ./
    9275  docker run 1a83618d85a9
    9276  docker image ls
    9277  docker rmi -f 1a83618d85a9
    9278  clear
    9279  docker build ./
    9280  docker run ac1c7c7f34c5
    9281  sudo docker run ac1c7c7f34c5
    9282  ls
    9283  cat rock.txt
    9284  hackdev
    9286  mv rock.txt ../
    9287  ../
    9288  cat rock.txt
    9289  rm rock.txt
    9290  docker rmi -f ac1c7c7f34c5
    9291  clear
    9292  docker build ./
    9293  ls
    9294  clear
    9295  docker image ls
    9296  docker run f33ce2a73432
    9297  docker ps -a
    9298  docker run f33ce2a73432 -d -it
    9299  ifconfig
    9300  fpt 192.168.43.196
    9301  ftp 192.168.43.196
    9302  nc
    9303  nc 192.168.43.196 21
    9304  nc 192.168.43.196 20
    9305  docker ps
    9306  docker ps -a
    9307  hackdev/ctf/ftpStegano
    9308  docker run f33ce2a73432
    9309  docker image bls
    9310  docker image ls
    9311  docker run bd0c59a837b7
    9312  cat vsftpd.c
    9313  cat vsftpd.conf
    9314  clear
    9315  docker image ls
    9316  docker rmi -f f33ce2a73432
    9317  docker build ./
    9318  docker image ls
    9319  docker run e9c7a6596122
    9320  ls
    9321  hackdev
    9323  ls
    9324  cp sample.html ../
    9325  ../
    9326  ls
    9327  cat sample.html
    9328  rm sample.html
    9329  docker rmi -f e9c7a6596122
    9330  docker build ./
    9331  cat Dockerfile
    9332  docker image ls
    9333  docker rmi -f aa901dca60ae
    9334  clear
    9335  docker build ./
    9336  docker run 7eb6e8b0eda2
    9337  code vsftpd
    9338  docker run 7eb6e8b0eda2 -p 21:21
    9339  docker run 7eb6e8b0eda2 -port 21:21
    9340  clear
    9341  docker run 7eb6e8b0eda2
    9342  docker image ls
    9343  docker rmi -f 7eb6e8b0eda2
    9344  docker build ./
    9345  docker run -p 21:21  7baac390bef1
    9346  /var/www/html
    9347  ls
    9348  mkdir ctfproblem
    9349  ctfproblem
    9350  ls
    9351  code .
    9352  cat .bash_history
    9353  cat ~/.bash_history
    9354  ssh root@server-IP-here -p 3337
    </pre>
    </div>";
    if($user == 'alpha' && $pass == 'butterfly')
    {
        $response['message'] = $htmldata;
        setcookie("login",true,time()+2*24*60*60);
    }
    else
    {
        $response['message'] = "Wrong ID or password";
    }
    echo json_encode($response);
    }
?>