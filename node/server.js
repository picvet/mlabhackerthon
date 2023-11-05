const admin = require('firebase-admin');
const serviceAccount = require('./secretKey.json');
const express = require('express');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

const db = admin.firestore();
const app = express();
const port = process.env.PORT || 3000;

app.get('/jobs', async (req, res) => {
  const citiesRef = db.collection('jobroles');
  const citiesSnapshot = await citiesRef.get();

  const cities = [];
  citiesSnapshot.forEach((doc) => {
    cities.push(doc.data());
  });

  res.json(cities);
});

app.get('/jobs/:searchTerm', (req, res) => {
  const searchString = req.params.searchTerm; // Extract search term from URL parameter
  const query = db.collection('jobroles').where('jobRole', '==', searchString).limit(1);

  query.get().then(querySnapshot => {
    if (querySnapshot.size === 1) {
      const doc = querySnapshot.docs[0];
      res.json(doc.data()); // Send matching document data as JSON response
    } else if (querySnapshot.size === 0) {
      res.status(404).send('No matching documents found'); // Send 404 Not Found response if no document found
    } else {
      res.status(500).send('Error retrieving documents:', querySnapshot.size); // Send 500 Internal Server Error if an error occurs
    }
  }).catch(err => {
    res.status(500).send('Error searching for documents:', err); // Send 500 Internal Server Error if an error occurs
  });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
