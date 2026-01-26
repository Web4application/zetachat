from virtualbox import VirtualBox

vbox = VirtualBox()

def import_ova(path):
    appliance = vbox.create_appliance()
    appliance.read(path)
    appliance.interpret()
    progress = appliance.import_machines()
    progress.wait_for_completion()
    return {"status": "imported", "file": path}
