const mongoose = require('mongoose');

const resumeSchema = new mongoose.Schema({
  studentId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  filename: {
    type: String,
    required: true
  },
  fileUrl: {
    type: String,
    required: true
  },
  filePath: String,
  fileSize: Number,
  contentType: String,
  extractedData: {
    name: String,
    email: String,
    phone: String,
    skills: [String],
    experience: String,
    education: [String],
    certifications: [String]
  },
  qualityScore: {
    type: Number,
    min: 0,
    max: 1,
    default: null
  },
  aiAnalysis: {
    strengths: [String],
    weaknesses: [String],
    suggestions: [String],
    analyzedAt: Date
  },
  uploadedAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model('Resume', resumeSchema);
