const mysql = require('mysql');

const connection = mysql.createConnection({
   host: 'localhost',
   user: 'Mozoomi',
   password: 'Dyzio26',
   database: 'factoCraftDB'
});

//connect
connection.connect((err) => {
   if(err){
      console.error("Error connectiong to data base: ", err);
      return;
   }
   console.log("Connected to MySql database");
});

// Perform a SELECT query
connection.query('SELECT * FROM factories', (err, results, fields) => {
   if (err) {
     console.error('Error executing SELECT query:', err);
     return;
   }
   console.log('SELECT query results:', results);
 });
 
 // Perform an INSERT query
 const newFactory = { name: 'New Factory', product: 'New Product', availability: true };
 connection.query('INSERT INTO factories SET ?', newFactory, (err, result) => {
   if (err) {
     console.error('Error executing INSERT query:', err);
     return;
   }
   console.log('New factory inserted with ID:', result.insertId);
 });
 
 // Perform an UPDATE query
 const updatedData = { product: 'Updated Product' };
 connection.query('UPDATE factories SET ? WHERE name = ?', [updatedData, 'New Factory'], (err, result) => {
   if (err) {
     console.error('Error executing UPDATE query:', err);
     return;
   }
   console.log('UPDATE query result:', result.affectedRows, 'row(s) updated');
 });
 
 // Perform a DELETE query
 connection.query('DELETE FROM factories WHERE name = ?', ['New Factory'], (err, result) => {
   if (err) {
     console.error('Error executing DELETE query:', err);
     return;
   }
   console.log('DELETE query result:', result.affectedRows, 'row(s) deleted');
 });
 
 // Close the database connection
 connection.end((err) => {
   if (err) {
     console.error('Error closing database connection:', err);
     return;
   }
   console.log('Database connection closed');
 });