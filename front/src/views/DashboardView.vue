<template>
  <v-app
    id="dashboard-view"
    class ="indigo lighten-4">
    <core-filter />

    <core-toolbar />

    <core-drawer />

    <v-content>
      <v-fade-transition mode="out-in">
        <router-view />
      </v-fade-transition>
    </v-content>

    <core-footer v-if="$route.meta.name !== 'Maps'" />

  </v-app>
</template>

<script>
export default {
  name: 'DashboardView',
  metaInfo () {
    return {
      title: 'Text generation'
    }
  }
}
</script>

<style>

</style>
