const express = require("express");
const JobRole = require("./jobRoleModel"); // Import the jobRoleSchema model

const router = express.Router();

// Define routes for creating, reading, updating, and deleting job roles using the jobRoleSchema model (CRUD operations).

// Example route for creating a job role
router.post("/", (req, res) => {
  const { name, sectors, requirements } = req.body;

  const newJobRole = new JobRole({
    name,
    sectors,
    requirements,
  });

  newJobRole.save((err) => {
    if (err) {
      console.error("Error saving job role:", err);
      res.status(500).send("Error saving job role");
    } else {
      console.log("Job role saved successfully.");
      res.status(201).json(newJobRole);
    }
  });
});

// Define other routes for reading, updating, and deleting job roles

module.exports = router;
