

def _update_context(self, context):
    # Append indices of errors to the "error" subcontext
    error_indices = []
    for i, field in enumerate(self.fields):
        if field.startswith("error_"):
            error_indices.append(i)

    # Add the "error" subcontext to the context
    context["error"] = {}
    for i in error_indices:
        context["error"][field] = {"index": i}

    # Add the "value" subcontext to the context
    context["value"] = {}
    for i in range(len(self.fields)):
        context["value"][field] = self.fields[i]
