# read_my_table.py
import boto3

REGION = "us-east-1"
TABLE_NAME = "Book"  # replace with your table name

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_item(item):
    # update these to match your attribute names
    title = item.get("Title", "Unknown")
    author = item.get("Author", "Unknown")
    genre = item.get("Genre", "Unknown")

    print(f"  Title  : {title}")
    print(f"  Author : {author}")
    print(f"  Genre  : {genre}")
    print()

def print_all_items():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No items found.")
        return

    print(f"Found {len(items)} item(s):\n")
    for item in items:
        print_item(item)

def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_items()

if __name__ == "__main__":
    main()