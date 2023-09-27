<template>
    <v-app>
        <header>
            <v-app-bar
            app
            color="grey"
            >
            <v-app-bar-title>
                <h3>iTEST</h3>
                <v-btn  flat to="/">Домой</v-btn>
                <v-btn  flat to="/about">Подробнее</v-btn>
            </v-app-bar-title>

            </v-app-bar>
        </header>

        <v-main class="cont">
            <slot/>
        </v-main>

        <v-footer>

        </v-footer>
    </v-app>
    
</template>

<script setup>
</script>

<style  scoped>
.v-container{
    display: flex;
}
</style>