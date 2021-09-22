import Vue from 'vue';
import Router from 'vue-router';
import Layout from '@/components/Layout/Layout';
import TablesBasicPage from '@/pages/Tables/Basic';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/app',
      name: 'Layout',
      component: Layout,
      children: [
        {
          path: 'tables',
          name: 'TablesBasicPage',
          component: TablesBasicPage,
        },
      ],
    },
  ],
});
