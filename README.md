# Keskivonfer
# Educational purposes only
### If you have any suggestions, please do not hesitate to contact us. 
Keskivonfer is a tool that allows you to extract information from a vinted account

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
### Demo
![](demo.gif)
## 💡 Prerequisite
   [Python 2/3](https://www.python.org/downloads/release/python-370/)
## 🛠️ Installation
### With PyPI
```pip3 install keskivonfer```
### With Github
```bash
git clone https://github.com/megadose/keskivonfer.git
cd keskivonfer/
python3 setup.py install
```
## 📚 Example
 - -u is the username
 - -v is the extension of the website .fr , .com, by default is .com
```bash
python3 Keskivonfer.py -u 12345678-monaccount -v fr
```
## 📈 Usage
The second argument is the extension of the site by default is .com
```python
from keskivonfer import *
print(getInfo("12345678-monaccount","be"))
```

## Thank you to :
- [ L003 ](https://twitter.com/L003_0S1N7)
## 📝 License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
