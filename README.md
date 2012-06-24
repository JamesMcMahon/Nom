## NOM
Nom is a simple app to store configuration and other files in a managed repo.

**NOTE:** _nom is still under active development and I'm not responible for anything_
_it may do to your files or pets._

Sample Usage:  

&nbsp;&nbsp;&nbsp;&nbsp;`nom add <file>` starts tracking a file  
&nbsp;&nbsp;&nbsp;&nbsp;`nom update <file>` updates the file in the managed repo  
&nbsp;&nbsp;&nbsp;&nbsp;`nom remove <file>` remove the file from managed repo

Commands:

* `add` -- add a file
* `update` -- update a file
* `remove` -- remove a file
* `revert` -- revert a file
* `status` -- check the status of a file

Dependencies:  

&nbsp;&nbsp;&nbsp;&nbsp;[GitPython](https://github.com/gitpython-developers/GitPython/) - for git storage
