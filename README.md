# AirBnB clone - The console

### Description
The console of the project AirBnB is a command line interface that the administrator can use to manipulate the database, you can add objects, update them or delete them etc...

### Utilisation
Start the console by typing: ./console
Close it by using: quit

Basic commands:
- create \<class>: create a new instance of this class
- show \<class> \<id>: print all attributes of an instance using it's class an id to find it
- update \<class> \<id> \<attribute name> \<value>: assign a value to an attribute
- all: print all instances
- destroy \<class> \<id>: delete an instance


###### Exemple:
	erwan@MSI:~/workdir/holbertonschool-AirBnB_clone$ ./console.py
	(hbnb) create User
	bd7b3b42-472d-4a6a-9ebb-b03ed1b64ad4
	(hbnb) all
	["[User] (bd7b3b42-472d-4a6a-9ebb-b03ed1b64ad4) {'created_at': datetime.datetime(2023, 11, 3, 12, 25, 1, 972348), 'updated_at': datetime.datetime(2023, 11, 3, 12, 25, 1, 972409), 'id': 'bd7b3b42-472d-4a6a-9ebb-b03ed1b64ad4'}"]
	(hbnb) update User bd7b3b42-472d-4a6a-9ebb-b03ed1b64ad4 name jean
	(hbnb) show User bd7b3b42-472d-4a6a-9ebb-b03ed1b64ad4
	[User] (bd7b3b42-472d-4a6a-9ebb-b03ed1b64ad4) {'created_at': datetime.datetime(2023, 11, 3, 12, 25, 1, 972348), 'updated_at': datetime.datetime(2023, 11, 3, 12, 27, 25, 733451), 'id': 'bd7b3b42-472d-4a6a-9ebb-b03ed1b64ad4', 'name': 'jean'}
	(hbnb) destroy User bd7b3b42-472d-4a6a-9ebb-b03ed1b64ad4
	(hbnb) all
	[]
	(hbnb) quit
	erwan@MSI:~/workdir/holbertonschool-AirBnB_clone$

### Requirements
Ubuntu: recommanded version: 20.04
Python: version 3

### Installation
git clone https://github.com/crasride/holbertonschool-AirBnB_clone.git


