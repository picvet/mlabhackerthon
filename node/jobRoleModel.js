const mongoose = require("mongoose");

// Define the schema for job roles
const jobRoleSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  sectors: {
    type: [String],
    required: true,
  },
  requirements: {
    skills: {
      type: [String],
      required: true,
    },
    education: {
      type: [String],
      required: true,
    },
  },
});

// Create a model based on the schema
const JobRole = mongoose.model("JobRole", jobRoleSchema);

module.exports = JobRole;
