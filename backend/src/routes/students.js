const express = require('express');
const router = express.Router();
const User = require('../models/User');

// Get student profile
router.get('/:id', async (req, res) => {
  try {
    const student = await User.findById(req.params.id).select('-password');
    res.json(student);
  } catch(err) {
    res.status(500).json({ error: err.message });
  }
});

// Update student profile
router.put('/:id', async (req, res) => {
  try {
    const student = await User.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.json(student);
  } catch(err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
