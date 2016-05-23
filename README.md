#Ola


If using amazones-ami:
sudo yum groupinstall "Development Tools"
sudo yum -y install gcc-c++ python27-devel atlas-sse3-devel lapack-devel
wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.2.tar.gz
tar xzf virtualenv-1.11.2.tar.gz 
python27 virtualenv-1.11.2/virtualenv.py sk-learn
. sk-learn/bin/activate
pip install numpy
easy_install six
pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.5.0-cp27-none-linux_x86_64.whl


Try using ami-e191b38b
