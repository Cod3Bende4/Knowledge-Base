# MarkdownCheatSheet
## Databases Operations
---
- Show all Databases: 
`show dbs`
- get current db:
`db`
- To create/switch to Database: `use <Database Name>`
- Delete/Drop Database (**Use with Caution** *First check current database by using `db` command*): `db.dropDatabase()`

## Collections Operations
---

- show collections: `show collections`
- create collection: `db.createCollection('<Collection Name>')`
- drop collection: `db.<Collection Name>.drop()`

## Rows/Fields Operations (Read)
---

- Show all rows in collection: `db.<Collection Name>.find()`
- Show all rows in collection (preetified): `db.<Collection Name>.find().pretty()`
- Search in MongoDB: `db.<Collection Name>.find(<field name>:<Search Parameter>)`
- **Less than/Greater than/ Less than or Eq/Greater than or Eq**
```
db.users.find({member_since: {$lt: 5}})
db.users.find({member_since: {$lte: 5}})
db.users.find({member_since: {$gt: 5}})
db.users.find({member_since: {$gte: 5}})
```
- Limiting number of search results print: `db.<Collection Name>.find().limit(<number of search results>)` *or*
  `db.<Collection Name>.findOne(<field name>:<Search Parameter>)`
- Counting number of search results: `db.<Collection Name>.find().count()`
- Sorting by fields in search results: `db.<Collection Name>.find().sort(<field name>:1)`

*if we want to do sorting in descending order then we will use **-1** in place of **1** in sort function*

---

## Rows/Fields Operations (Write)

- **Add document in collection**: `db.<Collection Name>.insert(<BSON Object>)`

*You can use multiple BSON object type in insert function for e.g.*

>Adding array of objects in collection

```
db.admin.insert([
    {
        'Name':'Rajesh',
        'Last_Logged':'12:00 PM',
    },
    {
        'Name':'BrijKishore',
        'Last_Logged':'01:00 PM',
    }
])
```
---
- **Updating existing rows** : `db.<Collection Name>.update ({<Search Param>},{Updated Parameters},{upsert:true})` 
*e.g.*
  
```
db.admin.update({Name:'Rajesh'},
{
    'Name':'New Rajesh',
    'Referrels': 2
    'Last_Logged':'12:55 PM',
    'Date':new Date()
},
{upsert:true})
```
*Enable upsert if you want to enable upsert if object is not found in the collection as per the search parameters*

*Use `updateMany` in place of `update` to apply it on multiple relevant fields*

---

- **Increment Value of a field data**: `db.<Collection Name>.update ({<Search Param>},{$inc: {Updated Parameters}})` *e.g.*
  
```
db.admin.update({Name:'Rajesh'},
{$inc:{
    'Referrels': 2
}})
```
---
- **Rename Value of a field name**: `db.<Collection Name>.update ({<Search Param>},{$rename: {Updated Parameters}})` *e.g.*

```
db.admin.updateMany({},
{$rename:{
    Last_Logged: 'last_logged_in'
}})
```
*if you want to rename all fields name then keep update function parameter empty*

---

- **Delete/Remove existing rows** : `db.<Collection Name>.remove({<Search Param>})` *e.g.*

```
db.admin.remove({Name:'Rajesh'})
```
---

>For more info go to : [Mongo DB Manual](https://docs.mongodb.com/manual/reference/operator/)
---
---
