from django.shortcuts import render
from django.http import JsonResponse
from .models import AssemblyProgram
from .utils import execute_assembly

def execute_assembly_view(request):
    if request.method == 'POST':
        program_id = request.POST.get('program_id')
        program_text = request.POST.get('program_text')

        result = execute_assembly(program_text)

        assembly_program = AssemblyProgram(program_id=program_id, program_text=program_text)
        if result is not None:
            assembly_program.success = True
            assembly_program.result = result
        assembly_program.save()

        return JsonResponse({'success': assembly_program.success, 'result': assembly_program.result})

    return render(request, 'index.html')
