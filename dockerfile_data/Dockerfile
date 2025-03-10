# 베이스 이미지
FROM ubuntu:22.04

# 메타데이터 추가
LABEL maintainer="rudwnzlxl6@naver.com"

RUN apt update -y && \
	apt install -y sudo passwd openssh-server wget && \
	apt install -y nano net-tools && \
	apt install -y iputils-ping openjdk-8-jdk python3-pip && \
	apt clean  && \ 
	rm -rf /var/lib/apt/lists/* 

#계정생성 및 세팅 
RUN groupadd lkjs && useradd -m -d /home/lkjs -s /bin/bash -g lkjs -G sudo lkjs && \
	echo "lkjs:1234" | chpasswd && \
	mkdir -p /home/lkjs/.ssh && \
	chown -R lkjs:lkjs /home/lkjs && \
	echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/lkjs/.bashrc && \
	chown lkjs:lkjs /home/lkjs/.bashrc && \
 	mkdir -p /var/run/sshd && \
 	echo "permitRootLogin no" >> etc/ssh/sshd_config && \
 	echo "passwrdAuthentication yes" >> /etc/ssh/sshd_config

#사용자 변경 
USER lkjs  
#작업환경 변경 
WORKDIR /home/lkjs
#pip 업그레이드 및 주피터랩 설치 
RUN pip install --upgrade pip && pip install jupyterlab 

#ssh 실행 및 주피터랩 가동(외부접속가능)
CMD ["/bin/bash","-c","service ssh start && python3 -m jupyterlab --ip=0.0.0.0 --port=8888 --allow-root"]