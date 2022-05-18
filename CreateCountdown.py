import bpy

FADE_TIME_IN = 5
#FADE_TIME_OUT = 5


# Hier muss auf jeden fall noch ein Textobjekt hin, dass ich erzeuge und die auswahl der Font

beginn = 1

fadeCube = bpy.data.objects['Fade_Control']
opacCube = bpy.data.objects['Opacity_Control']

print(fadeCube)

fadeCube.animation_data_clear()
opacCube.animation_data_clear()

for o in bpy.context.scene.objects:
    if o.name == "Fade_Control":
        print ("Cube found in scene")


currentFrame = beginn
for x in range (60):
    
    fadeCube.location[2] = 0
    fadeCube.keyframe_insert(data_path="location", frame=(currentFrame))
    
    
    opacCube.location[2] = 1
    opacCube.keyframe_insert(data_path="location", frame=(currentFrame))
    
    
    opacCube.location[2] = 0
    opacCube.keyframe_insert(data_path="location", frame=(currentFrame+FADE_TIME_IN))
    
    currentFrame = currentFrame + 20
    
    fadeCube.location[2] = 0
    fadeCube.keyframe_insert(data_path="location", frame=(currentFrame))
    
    currentFrame = currentFrame + 29
    
    fadeCube.location[2] = 0.55
    
    fadeCube.keyframe_insert(data_path="location", frame=(currentFrame))
    
    
    currentFrame = currentFrame + 1
    
    fadeCube.location[2] = 0
    
    fadeCube.keyframe_insert(data_path="location", frame=(currentFrame))
    
    print(currentFrame)


#####texte werden hier erzeugt

counter = 1
currentFrame = 50

#origobj
textobj =  bpy.data.objects.get('Text_57')

for x in range(60): 
    textobj.select_set(state=True)
    bpy.context.view_layer.objects.active = textobj
    bpy.ops.object.duplicate(linked=False)

    #alles deselektieren
    for obj in bpy.context.selected_objects:
        obj.select_set(False) 


    #selektiere das neu erzeugte Objet, keyframeanpassung    
    if (counter < 10): 
        nameTextObj = "Text_57.00" + str(counter)
    if (counter >= 10):
        nameTextObj = "Text_57.0" + str(counter)
    

    nuText = bpy.data.objects.get(nameTextObj)
    
    nuText.select_set(state=True)
    bpy.context.view_layer.objects.active = nuText
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    
    zahl = (60 - counter)
    zahlString = str(zahl)
    
    bpy.ops.font.text_insert(text=zahlString,accent=False)
    bpy.ops.object.editmode_toggle()
    
    ## konvertiere zum Mesh
    bpy.ops.object.convert(target="MESH")
    
    ## Bastel das Partikelsystem
    bpy.ops.object.particle_system_add()
    
    part = obj.particle_systems[0]
    settings = part.settings
    settings.emit_from = 'FACE'
    settings.frame_start = currentFrame
    settings.frame_end =  currentFrame + 15
    settings.lifetime = 32.00
    settings.count = 5000
    settings.particle_size = 0.025
    settings.render_type = 'OBJECT'
    settings.rotation_mode = 'VEL'
    settings.use_rotations = True
    settings.rotation_factor_random = 0.845
    settings.phase_factor = 0.0

    settings.render_type = 'OBJECT'
    settings.instance_object =  bpy.data.objects.get('Particle')  

    settings.effector_weights.gravity = 0
    settings.normal_factor = 0.025 # <----- hier Einstellen
        
    #Render Disabling und so
    
    nuText.hide_render = True
    nuText.hide_viewport = True
    nuText.keyframe_insert('hide_render', frame=currentFrame -1)
    nuText.keyframe_insert('hide_viewport', frame=currentFrame -1 )
    
    nuText.hide_render = False
    nuText.hide_viewport = False
    nuText.keyframe_insert('hide_render', frame=currentFrame )
    nuText.keyframe_insert('hide_viewport', frame=currentFrame) 

    currentFrame+= 50
    

    nuText.hide_render = True
    nuText.hide_viewport = True
    nuText.keyframe_insert('hide_render', frame=(currentFrame )) 
    nuText.keyframe_insert('hide_viewport', frame=(currentFrame))

    #currentFrame+=1
    counter+=1

textobj.hide_viewport = True
textobj.hide_render = True