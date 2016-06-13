from graphviz import Digraph


LATEST_ENTITY_VERSION = {}


def render_data_properties(props):
    """

    :param props:
    :return:
    """

    template = """<tr><td>%s</td></tr>"""

    return "".join([template % prop for prop in props])


def render_node_label(header, props):
    """

    :param header:
    :param props:
    :return:
    """

    template = """<
            <table cellspacing="0" border="0" cellborder="1">
                <tr><td><font point-size="16">%s</font></td></tr>
                %s
            </table>>"""

    return template % (header, render_data_properties(props))


def add_entity(g, name, props=None, **kwargs):
    if props is None:
        props = []
    LATEST_ENTITY_VERSION[name] = props[-1]
    g.node(name, render_node_label(name, props), **kwargs)


def add_relationship_edge(g, head, tail, label, **kwargs):
    kwa = kwargs
    if LATEST_ENTITY_VERSION[tail] != label:
        kwa.update({'color': 'red', 'penwidth': '2.0'})
    g.edge(head, tail, ' %s ' % label, **kwargs)


if __name__ == '__main__':
    g = Digraph('G', filename='dependencies.dot')

    g.attr('graph',
           label='Daedafusion Dependency Graph',
           fontsize='20',
           labeljust='l',
           labelloc='t')

    # entities
    g.attr('node',
           shape='plaintext',
           fontsize='12')

    add_entity(g, 'jetcd', [
    	'1.0',
    	'1.1-SNAPSHOT',
    ])
    add_entity(g, 'crypto', [
    	'1.0',
    ])
    add_entity(g, 'service-framework', [
    	'1.0',
    	'1.0.1',
    	'1.1-SNAPSHOT',
    ])
    add_entity(g, 'configuration', [
    	'1.0',
    	'1.1-SNAPSHOT',
    ])
    add_entity(g, 'cache', [
    	'1.0',
    ])
    add_entity(g, 'security-framework', [
    	'1.0',
    	'1.1-SNAPSHOT',
    ])
    add_entity(g, 'service-discovery', [
    	'1.0',
    	'1.1-SNAPSHOT',
    ])
    add_entity(g, 'service-bootstrap', [
    	'1.0',
    	'1.1-SNAPSHOT',
    ])
    add_entity(g, 'graph', [
    	'1.0',
    ])
    add_entity(g, 'hibernate-utils', [
    	'1.0',
    ])
    add_entity(g, 'events', [
    	'1.0',
    ])

    add_entity(g, 'aniketos', [
    	'1.0-SNAPSHOT',
    ])
    add_entity(g, 'knowledge', [
    	'1.0-SNAPSHOT',
    ])
    add_entity(g, 'infrastructure', [
    	'1.0-SNAPSHOT',
    ])


    # relationships
    g.attr('edge',
           color='gray50',
           minlen='2',
           style='dashed',
           dir='forward',
           arrowhead='halfopen')

    add_relationship_edge(g, 'service-framework', 'configuration', '1.1-SNAPSHOT')

    add_relationship_edge(g, 'cache', 'service-framework', '1.0')

    add_relationship_edge(g, 'security-framework', 'service-framework', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'security-framework', 'configuration', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'security-framework', 'crypto', '1.0')

    add_relationship_edge(g, 'service-discovery', 'configuration', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'service-discovery', 'jetcd', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'service-discovery', 'crypto', '1.0')

    add_relationship_edge(g, 'service-bootstrap', 'configuration', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'service-bootstrap', 'crypto', '1.0')
    add_relationship_edge(g, 'service-bootstrap', 'service-framework', '1.0')
    add_relationship_edge(g, 'service-bootstrap', 'security-framework', '1.0')

    add_relationship_edge(g, 'hibernate-utils', 'configuration', '1.0')

    add_relationship_edge(g, 'events', 'service-framework', '1.0')
    add_relationship_edge(g, 'events', 'configuration', '1.0')

    add_relationship_edge(g, 'aniketos', 'configuration', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'aniketos', 'crypto', '1.0')
    add_relationship_edge(g, 'aniketos', 'events', '1.0')
    add_relationship_edge(g, 'aniketos', 'hibernate-utils', '1.0')
    add_relationship_edge(g, 'aniketos', 'service-discovery', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'aniketos', 'security-framework', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'aniketos', 'service-bootstrap', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'aniketos', 'service-framework', '1.1-SNAPSHOT')

    add_relationship_edge(g, 'knowledge', 'configuration', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'knowledge', 'crypto', '1.0')
    add_relationship_edge(g, 'knowledge', 'cache', '1.0')
    add_relationship_edge(g, 'knowledge', 'graph', '1.0')
    add_relationship_edge(g, 'knowledge', 'events', '1.0')
    add_relationship_edge(g, 'knowledge', 'hibernate-utils', '1.0')
    add_relationship_edge(g, 'knowledge', 'service-discovery', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'knowledge', 'security-framework', '1.0')
    add_relationship_edge(g, 'knowledge', 'service-bootstrap', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'knowledge', 'service-framework', '1.1-SNAPSHOT')

    add_relationship_edge(g, 'infrastructure', 'configuration', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'infrastructure', 'crypto', '1.0')
    add_relationship_edge(g, 'infrastructure', 'cache', '1.0')
    add_relationship_edge(g, 'infrastructure', 'graph', '1.0')
    add_relationship_edge(g, 'infrastructure', 'events', '1.0')
    add_relationship_edge(g, 'infrastructure', 'aniketos', '1.0-SNAPSHOT')
    add_relationship_edge(g, 'infrastructure', 'hibernate-utils', '1.0')
    add_relationship_edge(g, 'infrastructure', 'service-discovery', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'infrastructure', 'security-framework', '1.0')
    add_relationship_edge(g, 'infrastructure', 'service-bootstrap', '1.1-SNAPSHOT')
    add_relationship_edge(g, 'infrastructure', 'service-framework', '1.1-SNAPSHOT')

    g.save()
