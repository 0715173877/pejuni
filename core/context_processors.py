from .models import FooterContent

def footer_context(request):
    """
    Context Processor to supply the global Footer settings to every template safely.
    It functions identically to a singleton.
    """
    footer_data = FooterContent.objects.first()
    return {'footer_data': footer_data}
