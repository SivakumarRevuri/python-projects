<p align="center"><img src="https://user-images.githubusercontent.com/113618658/196811951-6fd8dc05-5cb2-4040-b295-547fde0d040d.png" height="156px" width="156px"></p>
<h2 align="center"><b>QRNote</b></h2>

![Linux](https://img.shields.io/badge/Linux-Compatible-brightgreen.svg)
![Windows](https://img.shields.io/badge/Windows-Compatible-brightgreen.svg)
![MacOS](https://img.shields.io/badge/OSX-Compatible-brightgreen.svg)
![Docker](https://img.shields.io/badge/Docker-working-blue.svg)
![Python3](https://img.shields.io/badge/Python-Code-blue.svg)
![Web](https://img.shields.io/badge/HTML,CSS,JS-Code-blue.svg)

<p style="text-align: center;">Self Hosted Note taking app that saves notes in QR codes. "Why? Well, why not :)"</p>

<p style="text-align: center;">Works on all devices that can run Python or Docker</p>

## Features

- Create new notes and save them (as QR codes)
- Delete existing notes/QR codes
- View your existing notes (in QR codes)
- Launch a manual check and send messages (if the schedule matches the date)
- Background color can be changed with a button
- All features can be used from any device on the same network
- More to come...

## Installation and running

There are two ways to install it.
#### First method: Install dependencies and pull the repo

```bash
  git clone https://github.com/tdeerenberg/QRNote.git
  cd QRNote
  pip install -r requirements.txt
  python QRNote.py
```
#### Second method: Run via docker-compose
```bash
  git clone https://github.com/tdeerenberg/QRNote.git
  cd QRNote
  docker-compose up -d
```    

## Usage and configuration

Once runnning, go to `http://(local IP):(port)`. **The default port is 1440.** You can use ifconfig or ipconfig (depending on your device) or go to your settings application to find out what your local IP address is.

Then, enter the login credentials, which can be set in the `config.json` file. **The default username is `admin` and password `ChangeMe`.

The port on which QRNote runs can be changed in either `QRNote.py` on the last line: 
``` python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1440)
```
or if using docker in `docker-compose.yml` at:

```docker-compose.yml
    ports:
      - 1440:1440`
```
## Features to be developed 
- Multiple user support
- Extra funtionalities like changing the QR code color, edit your existing notes, etc.
- Option to download all notes
- Add the option to use MySQL for the login credentials for extra security
- If you have any features you would like to see, feel free to respond! (to do so, create an issue with "feature request" in the title)

## Demo
https://user-images.githubusercontent.com/113618658/196804436-b868cb95-af7b-466c-99fc-f4e70cdbe177.mp4

## Authors

- [@tdeerenberg](https://www.github.com/tdeerenberg)


## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. 
Footer
