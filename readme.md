# Local SQL Database Cleanup Script

This script is designed to delete all databases on your local MS-SQL instance. It's particularly useful for software support purposes when your local SQL instance gets bloated with many databases for different versions of software.

## Installation

To install requirements, run the following command in the directory:

```bash
pip install -r requirements.txt
```
## Configuration

1. Edit the `excluded_dbs.txt` file to include the databases you don't want to delete. Note that system databases are handled by the Python script and are not included here. Examples are provided in the file.

2. Ensure you have a user created in the server with permissions in the master database. For instance, you can create a user named `python` with appropriate permissions.

## Usage

Simply execute the script to delete all non-excluded databases:

```bash
python delete_databases.py
```

## Disclaimer

Be cautious while running this script as it will delete databases from your SQL instance. Make sure you have appropriate backups or precautions in place before executing it.
