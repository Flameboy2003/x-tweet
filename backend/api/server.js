const express = require('express');
const { MongoClient } = require('mongodb');
const cors = require('cors');

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB connection
const mongoUrl = "mongodb://localhost:27017/";
const dbName = "twitter_trends";
const collectionName = "trends_by_hour";

let db, collection;

async function connectToMongo() {
  const client = new MongoClient(mongoUrl);
  try {
    await client.connect();
    db = client.db(dbName);
    collection = db.collection(collectionName);
    console.log("Connected to MongoDB");
  } catch (error) {
    console.error("MongoDB connection error:", error);
    process.exit(1);
  }
}

// API endpoint to get trends
app.get('/api/trends', async (req, res) => {
  try {
    const pipeline = [
      { $sort: { timestamp: -1 } }, // Sort by timestamp descending
      { $limit: 6 }, // Get last 6 hours
      {
        $project: {
          _id: 1,
          timestamp: 1,
          country: 1,
          trends: 1
        }
      }
    ];
    
    const cursor = collection.aggregate(pipeline);
    const results = await cursor.toArray();
    
    res.json(results);
  } catch (error) {
    console.error("Error fetching trends:", error);
    res.status(500).json({ error: "Failed to fetch trends" });
  }
});

// Start server
connectToMongo().then(() => {
  app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
  });
});