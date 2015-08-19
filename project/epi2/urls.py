from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import api, views


router = DefaultRouter()
router.register(r'study-population', api.StudyPopulation, base_name="study-population")
router.register(r'outcome', api.Outcome, base_name="outcome")
router.register(r'groups', api.GroupCollection, base_name="groups")
router.register(r'group', api.Group, base_name="group")


urlpatterns = [

    url(r'^api/', include(router.urls, namespace='api')),

    # Criteria
    url(r'^assessment/(?P<pk>\d+)/study-criteria/create/$',
        views.StudyCriteriaCreate.as_view(),
        name='studycriteria_create'),

    # Study population
    url(r'^study/(?P<pk>\d+)/study-population/create/$',
        views.StudyPopulationCreate.as_view(),
        name='sp_create'),
    # url(r'^study/(?P<pk>\d+)/study-population/copy-as-new-selector/$',
    #     views.StudyPopulationCopyAsNewSelector.as_view(),
    #     name='sp_copy_selector'),
    url(r'^study-population/(?P<pk>\d+)/$',
        views.StudyPopulationDetail.as_view(),
        name='sp_detail'),
    url(r'^study-population/(?P<pk>\d+)/update/$',
        views.StudyPopulationUpdate.as_view(),
        name='sp_update'),
    url(r'^study-population/(?P<pk>\d+)/delete/$',
        views.StudyPopulationDelete.as_view(),
        name='sp_delete'),

    # Adjustment factor
    url(r'^assessment/(?P<pk>\d+)/factors/create/$',
        views.AdjustmentFactorCreate.as_view(),
        name='af_create'),

    # Outcome
    url(r'^study-population/(?P<pk>\d+)/outcome/create/$',
        views.OutcomeCreate.as_view(),
        name='outcome_create'),
    # url(r'^exposure/(?P<pk>\d+)/outcome/copy-as-new-selector/$',
    #     views.OutcomeCopyAsNewSelector.as_view(),
    #     name='outcome_copy_selector'),
    url(r'^outcome/(?P<pk>\d+)/$',
        views.OutcomeDetail.as_view(),
        name='outcome_detail'),
    url(r'^outcome/(?P<pk>\d+)/update/$',
        views.OutcomeUpdate.as_view(),
        name='outcome_update'),
    url(r'^outcome/(?P<pk>\d+)/delete/$',
        views.OutcomeDelete.as_view(),
        name='outcome_delete'),

    # Group collection
    url(r'^study-population/(?P<pk>\d+)/groups/create/$',
        views.GroupCollectionCreate.as_view(),
        name='gc_create'),
    # url(r'^exposure/(?P<pk>\d+)/outcome/copy-as-new-selector/$',
    #     views.OutcomeCopyAsNewSelector.as_view(),
    #     name='outcome_copy_selector'),
    url(r'^groups/(?P<pk>\d+)/$',
        views.GroupCollectionDetail.as_view(),
        name='gc_detail'),
    url(r'^groups/(?P<pk>\d+)/update/$',
        views.GroupCollectionUpdate.as_view(),
        name='gc_update'),
    url(r'^groups/(?P<pk>\d+)/delete/$',
        views.GroupCollectionDelete.as_view(),
        name='gc_delete'),

    url(r'^group/(?P<pk>\d+)/$',
        views.GroupDetail.as_view(),
        name='g_detail'),
    url(r'^group/(?P<pk>\d+)/update/$',
        views.GroupUpdate.as_view(),
        name='g_update'),

]
