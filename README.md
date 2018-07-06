# Hugin_scripts
Converts photos taken by Samsung gear 360 to different projections

## Add to $PATH
add ```export PATH="<Path_to_the_/bin/v2712_directory>:$PATH"```
on the last line in the ```~/.bashrc``` file
remember to ```source ~/.bashrc``` afterwards

## Example script usage
```
  fish2equi_v2712.py <Path_to_file>
```

## Dependencies


```export PATH="/home/vagrant/Hugin_scripts/bin/v2712:$PATH"```

Python2:
	```sudo apt-get install python-minimal```

Pip:
	```sudo apt-get update```
	```sudo apt-get -y upgrade```
	```sudo apt-get install python-pip```
	```export LC_ALL=C```
	```pip install --upgrade pip```
	```pip2 --version```

Packages:
	```sudo pip2 install Pillow```
	```sudo pip2 install numpy```

Hugin:
	```sudo apt install hugin_tools```
	```sudo add-apt-repository ppa:ubuntuhandbook1/apps```
	```sudo apt-get update```
	```sudo apt-get install hugin```

Convert:
	```sudo apt install imagemagick```

cubic2erect:
	```sudo apt update```

	```sudo apt install make```

	```sudo apt install -y cpanminus```
	
	sudo cpan
	  ```cpan[1]> yes```
	  ```cpan[1]> [paina enter]```
	  ```cpan[1]> yes```
	  # Spam these as many times as necessary to complete installation
	  ```cpan[1]> install Panotools::Script```
	  ```cpan[1]> install Panotools::Script::Line::Variable```

	```sudo add-apt-repository ppa:hugin/hugin-builds```
	```sudo apt-get update```
	```sudo apt-get install -y hugin enblend```
