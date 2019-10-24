10/23/2019 Installed Python to work with Google TensorFlow

https://www.tensorflow.org/install/pip

https://github.com/Serendipity-007/TensorFlowTest



1. Install Python
https://chocolatey.org/packages/python

choco install python -y

Note: We can save ourselves some trouble later on by installing Python 3.6.8 right out of the gate (TensorFlow supports only Python 3.6 and v3.6.8 is the last 3.6.x on Chocolatey)

choco install python -y --version=3.6.8



2. Check versions

python3 --version
pip3 --version
virtualenv --version



3. Install Virtualenv

Run PowerShell as Administrator

pip3 install -U pip virtualenv



4. Test Virtualenv again

Run PowerShell as user

virtualenv --version



5. Enable long paths in Windows via Group Policy
https://superuser.com/questions/1119883/windows-10-enable-ntfs-long-paths-policy-option-missing

gpedit.msc
Local Computer Policy > Computer Configuration > Administrative Templates > System > Filesystem > Enable Win32 long paths



6. Install 'Visual C++ 2015 Redistributable Update 3'
Already in place if Visual Studio is installed



7. Create virtual environment
https://www.tensorflow.org/install/pip#2.-create-a-virtual-environment-recommended

Create a working directory for projects
Open a Bash window (e.g. Git Bash)

cd G:\Desktop\testing

virtualenv --system-site-packages -p python3 ./venv

(May need to reference a different Python executable if running multiple side-by-side, in which case the command might be as follows:)

virtualenv --system-site-packages -p  python ./venv

(If a 'venv' directory is not created in the test project directory, try a command with fewer parameters:)

virtualenv ./venv

zac@Resilience MINGW64 /g/Desktop/testingpython
$ virtualenv --system-site-packages -p python3 ./venv
Running virtualenv with interpreter C:\Users\zac\AppData\Local\Microsoft\WindowsApps\python3.exe



8. Activate the virtual environment
https://stackoverflow.com/questions/57318343/virtualenv-v16-7-2-powershell-activate-script-you-must-source-this-script-p

Create a 'source' directory so that there will be a tidy .git, source/, venv/ and .gitignore in the project root folder
mkdir source

source venv/Scripts/activate

(Original instructions skip the 'source' subdirectory, in which case the following (a period) is used) . venv/Scripts/activate

Check versions again now that we are running in a virtual environment:

python3 --version
python --version (alternate depending on installed versions)
pip3 --version
virtualenv --version



9. "Install packages within a virtual environment without affecting the host system setup. Start by upgrading pip:"

pip install --upgrade pip

zac@Resilience MINGW64 /g/Desktop/testingpython
$ pip install --upgrade pip
Requirement already up-to-date: pip in g:\desktop\testingpython\venv\lib\site-packages (19.3.1)
(venv)



10. "show packages installed within the virtual environment"

pip list



11. Keep in mind for later on, "And to exit virtualenv later:"

deactivate  # don't exit until you're done using TensorFlow




12. Install the TensorFlow pip package
https://www.tensorflow.org/install/pip#3.-install-the-tensorflow-pip-package
Chosen package: tensorflow (not tensorflow-gpu)
Chosen environment: 'Virtualenv install' (not System install)

pip install --upgrade tensorflow
pip install tensorflow

zac@Resilience MINGW64 /g/Desktop/testingpython
$ pip install --upgrade tensorflow
ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
ERROR: No matching distribution found for tensorflow

The above error probably means the Python vesion is not 3.6[.8] in which case follow the next step to install 3.6.8 side-by-side with 3.8 (the current version used by Chocolatey)



13. Install Python 3.6
https://stackoverflow.com/questions/38896424/tensorflow-not-found-using-pip
Comment: "For me this happens with python 3.7, After hours of struggle I used 3.6 and that worked." (https://stackoverflow.com/questions/38896424/tensorflow-not-found-using-pip#comment91410599_38896424)
https://chocolatey.org/packages/python/3.6.8

Run PowerShell as Administrator

choco install python -y --version=3.6.8 --allow-downgrade

This will install C:\Python36 alongside C:\Python38



14. Reinitialize virtualenv pointing at Python 3.6

Return to a Bash window or Command Prompt

virtualenv . -p python

zac@Resilience MINGW64 /g/Desktop/testingpython
$ virtualenv . -p python
Already using interpreter C:\Python36\python.exe
Using base prefix 'C:\\Python36'
New python executable in G:\Desktop\testingpython\Scripts\python.exe
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter C:\Python36\python.exe


15. Check virtual environment again

pip list

zac@Resilience MINGW64 /g/Desktop/testingpython
$ pip list
Package    Version
---------- -------
pip        18.1
setuptools 40.6.2
You are using pip version 18.1, however version 19.3.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.



16. Repeat prior step ("Start by upgrading pip:")

pip install --upgrade pip

Must run command in Bash as Administrator



17. Install TensorFlow package

pip install --upgrade tensorflow

Verify the install:

python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

Outputs something like:
tf.Tensor(2045.3495, shape=(), dtype=float32)



18. Troubleshooting

List of virtualenv commands for troubleshooting:

mkdir source
virtualenv --system-site-packages -p python3 ./venv
virtualenv -p python3 ./venv
virtualenv ./venv
python --version
source venv/Scripts/activate
deactivate
rm -r venv/
virtualenv --system-site-packages -p  python ./venv
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps (this is the location the PATH environment variable gets e.g. 'python' and 'python3' from; multiple versions of Python here can cause trouble but that is the point of virtual environments

https://www.freecodecamp.org/news/installing-multiple-python-versions-on-windows-using-virtualenv/
https://stackoverflow.com/questions/37137664/issue-with-activating-virtualenv
https://github.com/github/gitignore/blob/master/Python.gitignore (shows that best practice is to use venv/ as the virtualenv directory)

Finally working:

cd source
python --version

zac@Resilience MINGW64 /g/Websites/Projects/Python/HelloWorld/source
$ python --version
Python 3.6.8
(venv)

Test out Python:
python -c "print('Hello World')"

Create and run a Python 'Hello World' file:
echo "print('Hello, World.')" > helloworld.py
python helloworld.py



19. Initialize Git

cd G:\Desktop\testing (this directory should have two folders: 'source', 'venv')

git init



20. Create a .gitignore file
https://github.com/github/gitignore/blob/master/Python.gitignore

touch .gitignore
echo "venv/" >> .gitignore



21. Start writing code

git status

git commit -am "initial commit"



22. Final directory structure:

G:\Websites\Projects\Python\TensorFlowTest\.git
G:\Websites\Projects\Python\TensorFlowTest\source
G:\Websites\Projects\Python\TensorFlowTest\source\helloworld.py
G:\Websites\Projects\Python\TensorFlowTest\venv
G:\Websites\Projects\Python\TensorFlowTest\.gitignore



23. Next steps:
https://www.tensorflow.org/tutorials/
https://www.tensorflow.org/tutorials/quickstart/beginner <-- "import tensorflow as tf" "from tensorflow import keras"
https://www.tensorflow.org/tutorials/keras/classification