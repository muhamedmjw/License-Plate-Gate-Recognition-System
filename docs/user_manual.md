# User Manual

## Getting Started

### Launching the Application

1. **Activate your virtual environment:**
   ```bash
   # On Windows:
   license_plate_env\Scripts\activate
   
   # On macOS/Linux:
   source license_plate_env/bin/activate
   ```

2. **Run the application:**
   ```bash
   python src/main.py
   ```

3. **The main window will open** showing the License Plate Recognition System interface.

## Main Interface

### Camera Section
- **Camera Preview:** Shows live feed from your camera
- **Start/Stop Camera:** Controls camera operation
- **Capture:** Takes a snapshot for processing
- **Settings:** Adjust camera parameters

### Detection Results
- **Live Results:** Shows detected license plates in real-time
- **Confidence Score:** Indicates detection accuracy (0-100%)
- **Plate Text:** Extracted text from the license plate
- **Timestamp:** When the detection occurred

### Database Panel
- **Recent Detections:** List of recently detected plates
- **Search Function:** Find specific plates by text or date
- **Export Data:** Save results to CSV file

## Step-by-Step Usage

### 1. First Time Setup

**Check Camera Connection:**
- Ensure your camera is connected and working
- Click "Start Camera" to begin live feed
- You should see yourself in the camera preview

**Adjust Camera Settings:**
- Position camera for optimal view
- Ensure good lighting conditions
- Adjust focus if your camera supports it

### 2. Detecting License Plates

**Automatic Detection:**
- With camera running, position a license plate in view
- The system automatically detects and processes plates
- Results appear in the Detection Results panel

**Manual Capture:**
- Click "Capture" to take a specific photo
- The system will process this image
- Results will be displayed and saved

**Optimal Conditions:**
- Good lighting (avoid shadows)
- Plate should be clearly visible
- Front-facing view works best
- Clean, unobstructed plate

### 3. Viewing Results

**Real-time Display:**
- Detected plates appear immediately
- Confidence score shows accuracy
- Timestamp records when detected

**Database Storage:**
- All detections are automatically saved
- Access through the Database Panel
- Search by plate number or date

## Features Guide

### Camera Operations

**Starting the Camera:**
1. Click "Start Camera" button
2. Grant camera permissions if prompted
3. Live feed appears in preview window

**Camera Settings:**
- **Resolution:** Adjust image quality
- **FPS:** Control frame rate
- **Brightness/Contrast:** Enhance image quality

**Troubleshooting Camera:**
- If no image appears, check camera connection
- Try different camera indices (0, 1, 2...)
- Restart application if camera freezes

### Detection Process

**How It Works:**
1. **Image Capture:** System captures frames from camera
2. **Plate Detection:** Locates license plates in the image
3. **Perspective Correction:** Straightens angled plates
4. **Text Recognition:** Extracts text using OCR
5. **Validation:** Checks if text looks like a license plate
6. **Storage:** Saves results to database

**Detection Indicators:**
- **Green Box:** Successful detection
- **Red Box:** Detection failed validation
- **Yellow Box:** Low confidence detection

### Database Management

**Viewing Records:**
- All detections appear in the database panel
- Shows plate number, timestamp, and confidence
- Click on record to view full details

**Searching:**
- Enter plate number in search box
- Use date filters to find specific timeframes
- Clear search to show all records

**Exporting Data:**
- Click "Export" to save data as CSV
- Choose location and filename
- File includes all detection details

### Advanced Features

**Batch Processing:**
- Process multiple images at once
- Drag and drop images onto the interface
- Results processed automatically

**Settings Configuration:**
- Adjust detection sensitivity
- Change OCR language settings
- Modify database storage options

## Tips for Best Results

### Camera Positioning
- **Distance:** 3-10 feet from license plate
- **Angle:** Straight-on view preferred
- **Height:** Camera at plate level
- **Stability:** Use tripod or stable surface

### Lighting Conditions
- **Natural Light:** Daylight works best
- **Avoid Glare:** Position to minimize reflections
- **Even Lighting:** Avoid harsh shadows
- **Indoor Use:** Ensure adequate lighting

### License Plate Conditions
- **Clean Plates:** Remove dirt and obstructions
- **Good Contrast:** Dark text on light background
- **Undamaged:** Avoid bent or damaged plates
- **Standard Format:** Works best with standard plates

## Troubleshooting

### Common Issues

**Camera Not Working:**
- Check camera connection
- Verify camera permissions
- Try different camera index
- Restart application

**Poor Detection Accuracy:**
- Improve lighting conditions
- Clean camera lens
- Position camera properly
- Check plate visibility

**Text Recognition Errors:**
- Ensure plate is clean and clear
- Improve camera focus
- Check lighting conditions
- Try different angles

**Database Issues:**
- Check database file permissions
- Verify disk space available
- Restart application
- Check database integrity

### Performance Tips

**Improve Speed:**
- Close unnecessary applications
- Use lower camera resolution
- Reduce detection frequency
- Optimize lighting conditions

**Improve Accuracy:**
- Use higher resolution camera
- Ensure stable camera mount
- Improve lighting setup
- Clean license plates

## Understanding Results

### Confidence Scores
- **90-100%:** Excellent detection, very reliable
- **80-89%:** Good detection, mostly reliable
- **70-79%:** Fair detection, may need verification
- **Below 70%:** Poor detection, likely inaccurate

### Text Validation
- System checks if detected text looks like a license plate
- Validates format and character patterns
- Filters out false positives
- Marks uncertain detections

### Database Records
Each detection includes:
- **Plate Number:** Extracted text
- **Timestamp:** When detected
- **Confidence:** Accuracy score
- **Image Path:** Location of captured image
- **Status:** Validation result

## Maintenance

### Regular Tasks
- **Clean Camera:** Remove dust and fingerprints
- **Check Lighting:** Ensure consistent illumination
- **Database Backup:** Export data regularly
- **Update Software:** Keep dependencies current

### Storage Management
- **Image Files:** Stored in data/images/
- **Database:** SQLite file in data/database/
- **Logs:** Application logs in data/logs/
- **Cleanup:** Remove old files periodically

## Advanced Usage

### Custom Settings
- Modify config/settings.py for advanced options
- Adjust detection parameters
- Change database settings
- Customize GUI appearance

### Integration
- Use API functions for custom applications
- Export detection functions for other projects
- Integrate with existing systems
- Extend functionality as needed

## Getting Help

### If You Need Assistance
1. Check this user manual
2. Review error messages in logs
3. Verify installation requirements
4. Check camera and lighting setup
5. Consult technical documentation

### Error Messages
- Most errors are displayed in the GUI
- Check logs for detailed error information
- Common issues have specific solutions
- Contact support if problems persist

---

**Remember:** This is a learning project designed to demonstrate computer vision concepts. Focus on understanding how the system works rather than achieving perfect accuracy in all conditions.