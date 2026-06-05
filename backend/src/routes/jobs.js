const express = require('express');
const router = express.Router();
const Job = require('../models/Job');

// Get all jobs
router.get('/', async (req, res) => {
  try {
    const jobs = await Job.find({ status: 'active' });
    res.json(jobs);
  } catch(err) {
    res.status(500).json({ error: err.message });
  }
});

// Get job by id
router.get('/:id', async (req, res) => {
  try {
    const job = await Job.findById(req.params.id);
    res.json(job);
  } catch(err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
