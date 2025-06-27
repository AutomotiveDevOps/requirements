from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'components/table_key_value/index.jinja'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_key_value_pair = resolve('key_value_pair')
    l_0_view_object = resolve('view_object')
    try:
        t_1 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    def macro():
        t_2 = []
        pass
        return concat(t_2)
    caller = Macro(environment, macro, None, (), False, False, False, context.eval_ctx.autoescape)
    yield context.call(environment.extensions['strictdoc.export.html.html_templates.AssertExtension']._assert, t_1((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair)), None, caller=caller)
    yield '\n\n'
    if t_1(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Section')):
        pass
        yield '\n  <div class="sdoc-table_key_value-section">'
        yield escape(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Section'))
        yield '</div>\n'
    else:
        pass
        yield '\n  '
        if (context.call(environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'project_config'), 'is_activated_search')) and t_1(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Link'))):
            pass
            yield '\n    <a\n      class="sdoc-table_key_value-key"\n      data-testid="search-'
            yield escape(context.call(environment.getattr(context.call(environment.getattr(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Key'), 'lower')), 'replace'), ' ', '-'))
            yield '"\n      href="'
            yield escape(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Link'))
            yield '">'
            yield escape(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Key'))
            yield '\n    </a>\n  '
        else:
            pass
            yield '\n    <div class="sdoc-table_key_value-key">'
            yield escape(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Key'))
            yield '</div>\n  '
        yield '\n  <div class="sdoc-table_key_value-value" data-testid="table-row-value-'
        yield escape(context.call(environment.getattr(context.call(environment.getattr(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Key'), 'lower')), 'replace'), ' ', '-'))
        yield '">'
        yield escape(environment.getitem((undefined(name='key_value_pair') if l_0_key_value_pair is missing else l_0_key_value_pair), 'Value'))
        yield '</div>\n'

blocks = {}
debug_info = '1=19&3=26&4=29&6=34&9=37&10=39&13=46&15=49'