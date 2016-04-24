from crudbuilder.abstract import BaseCrudBuilder

from app1.models import Post


class PersonCrud(BaseCrudBuilder):
    model = Post
    search_feilds = ['name']
    tables2_fields = ('name',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 10
    modelform_excludes = ['created_by', 'updated_by']
    login_required = True

    custom_templates = {
        'list': 'person_list.html'
    }
