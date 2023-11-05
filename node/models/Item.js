const mongoose = require("mongoose");

// Define the schema
const jobRoleSchema = new mongoose.Schema({
  name: String,
  sectors: [String],
  requirements: {
    skills: [String],
    education: [String],
  },
});

// Create a model based on the schema
const JobRole = mongoose.model("JobRole", jobRoleSchema);

module.exports = JobRole;