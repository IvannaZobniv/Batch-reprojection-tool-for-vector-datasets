import arcpy
import os

arcpy.env.overwriteOutput = True
targetFC = arcpy.GetParameterAsText(0)
folderToExamine = r"D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_2\PE\Lesson2\Project.gdb"


#get spatial reference for the target feature class
targetDescribe = arcpy.Describe(targetFC)
targetSR = targetDescribe.SpatialReference
targetSRName = targetSR.Name

# Get a list of my feature classes
arcpy.env.workspace = folderToExamine
listOfFCs = arcpy.ListFeatureClasses()
    #Loop through the list of FCs  
for currentFC in listOfFCs:
    print (currentFC)
        #Read the spatial reference of the current one
    currentFCDescribe = arcpy.Describe(currentFC)
    currentFCSR = currentFCDescribe.SpatialReference
    currentFCSRName = currentFCSR.Name
    print (currentFCSRName)

    if currentFCSRName != targetSRName:
        print ("Spatial references don't match")
    else:
        print ("Spatial references do match")   
    if currentFCSRName == targetSRName:
    #skip
        continue
    else:
    # Determine the new output feature class path and name
        outCS = currentFC[:-4] +"_projected.shp"
        arcpy.Project_management(currentFC, outCS, targetSR)
        arcpy.AddMessage("All done!")
else:
    arcpy.AddMessage(arcpy.GetMessages())

