    _   ______  __  ___
   / | / / __ \/  |/  /
  /  |/ / / / / /|_/ / 
 / /|  / /_/ / /  / /  
/_/ |_/\____/_/  /_/   
***
Nom is a simple app to store configuration and other files in a managed repo.

NOTE: nom is still under active development and I'm not responible for anything
it may do to your files or pets.

Sample Usage:
	`nom add <file>`, starts tracking a file
	`nom update <file>`, updates the file in the managed repo
	`nom remove <file>`, remove the file from managed repo

Commands:
	`add` -- add a file
	`update` -- update a file
	`remove` -- remove a file
	`revert` -- revert a file
	`status` -- check the status of a file

Dependencies:
	gitpython - for git storage

