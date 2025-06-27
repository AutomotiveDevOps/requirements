from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'screens/project_statistics/main.jinja'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_view_object = resolve('view_object')
    try:
        t_1 = environment.tests['none']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'none' found.")
    pass
    yield '<div class="main">\n\n<div class="sdoc-table_key_value">\n\n'
    l_1_key_value_pair = {'Section': 'General information'}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Project name', 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'project_config'), 'project_title')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Statistics generation date', 'Value': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'get_datetime'))}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Last modification of project data', 'Value': context.call(environment.getattr(environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'traceability_index'), 'strictdoc_last_update'), 'strftime'), '%Y-%m-%d %H:%M:%S')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Git commit/release', 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'git_commit_hash')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Total documents', 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'total_documents')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Section': 'Sections'}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Total sections', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=node.is_section'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'total_sections')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Sections without any text', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=(node.is_section and not node.contains_any_text)'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'sections_without_text_nodes')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Section': 'Requirements'}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Total requirements', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=node.is_requirement'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'total_requirements')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Requirements with no UID', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=(node.is_requirement and node["UID"] == None)'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'requirements_no_uid')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Root-level requirements not connected to by any requirement', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=(node.is_requirement and node.is_root and node["STATUS"] != "Backlog" and not node.has_child_requirements)'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'requirements_root_no_links')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Non-root-level requirements not connected to any parent requirement', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=(node.is_requirement and not node.is_root and node["STATUS"] != "Backlog" and not node.has_parent_requirements)'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'requirements_no_links')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Requirements with no RATIONALE', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=(node.is_requirement and node["RATIONALE"] == None)'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'requirements_no_rationale')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    if context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_status_have_status')):
        pass
        yield '\n\n'
        l_1_key_value_pair = {'Section': 'Requirements status breakdown'}
        pass
        yield '\n  '
        template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
        gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
        try:
            for event in gen:
                yield event
        finally: gen.close()
        yield '\n'
        l_1_key_value_pair = missing
        yield '\n\n'
        for (l_1_status_, l_1_status_count_) in context.call(environment.getattr(environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'requirements_status_breakdown'), 'items')):
            l_1_status_query_value = missing
            _loop_vars = {}
            pass
            yield '\n  \n  '
            l_1_status_query_value = (markup_join(('"', l_1_status_, '"', )) if (not t_1(l_1_status_)) else 'None')
            _loop_vars['status_query_value'] = l_1_status_query_value
            yield '\n\n  '
            l_2_key_value_pair = {'Key': markup_join(('Requirements with status ', l_1_status_, )), 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), (('search?q=(node.is_requirement and node["STATUS"] == ' + (undefined(name='status_query_value') if l_1_status_query_value is missing else l_1_status_query_value)) + ')'), _loop_vars=_loop_vars), 'Value': l_1_status_count_}
            pass
            yield '\n    '
            template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
            gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_2_key_value_pair, 'status_': l_1_status_, 'status_count_': l_1_status_count_, 'status_query_value': l_1_status_query_value}))
            try:
                for event in gen:
                    yield event
            finally: gen.close()
            yield '\n  '
            l_2_key_value_pair = missing
            yield '\n'
        l_1_status_ = l_1_status_count_ = l_1_status_query_value = missing
        yield '\n\n'
    yield '\n\n'
    l_1_key_value_pair = {'Section': 'TBD/TBC'}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Total TBD', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=node.contains("TBD")'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'total_tbd')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n'
    l_1_key_value_pair = {'Key': 'Total TBC', 'Link': context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_url'), 'search?q=node.contains("TBC")'), 'Value': environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document_tree_stats'), 'total_tbc')}
    pass
    yield '\n  '
    template = environment.get_template('components/table_key_value/index.jinja', 'screens/project_statistics/main.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'key_value_pair': l_1_key_value_pair}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'
    l_1_key_value_pair = missing
    yield '\n\n</div>\n\n</div>'

blocks = {}
debug_info = '10=22&19=34&28=46&37=58&46=70&55=82&61=94&71=106&81=118&87=130&97=142&107=154&117=166&127=178&137=190&140=199&145=205&148=214&152=219&161=225&170=240&180=252&190=264'