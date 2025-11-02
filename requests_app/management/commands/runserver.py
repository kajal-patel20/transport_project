import sys
from io import StringIO
from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.servers.basehttp import WSGIServer


class Command(RunserverCommand):
    """Custom runserver command that suppresses HTTPS probe warnings and shows localhost."""
    
    def inner_run(self, *args, **options):
        
        from django.core.servers.basehttp import WSGIRequestHandler
        original_log_message = WSGIRequestHandler.log_message
        
        def quiet_log_message(self, format, *args):
            message = format % args
            
            if "HTTPS" not in message and "supports HTTP" not in message and "Bad request" not in message:
                original_log_message(self, format, *args)
        
        WSGIRequestHandler.log_message = quiet_log_message
        
        
        if options['addrport'] == 'localhost:8000':
            
            original_stdout_write = sys.stdout.write
            
            def custom_write(text):
                
                text = text.replace('http://127.0.0.1:8000/', 'http://localhost:8000/')
                text = text.replace('127.0.0.1:8000', 'localhost:8000')
                return original_stdout_write(text)
            
            sys.stdout.write = custom_write
        
        super().inner_run(*args, **options)
