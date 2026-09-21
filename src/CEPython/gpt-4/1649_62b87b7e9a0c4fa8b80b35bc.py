

def _update_context(self, context):
    # Check if 'error' key exists in context, if not, create it
    if 'error' not in context:
        context['error'] = {}

    # Check if 'x_low', 'y_low', 'z_low' keys exist in context['error'], if not, create them
    for key in ['x_low', 'y_low', 'z_low']:
        if key not in context['error']:
            context['error'][key] = {"index": []}

    # Check if 'E', 't', 'error_E_low' exist in the graph's properties
    if hasattr(self, 'E'):
        context['error']['x_low']['index'].append(self.E)
    if hasattr(self, 't'):
        context['error']['y_low']['index'].append(self.t)
    if hasattr(self, 'error_E_low'):
        context['error']['z_low']['index'].append(self.error_E_low)
