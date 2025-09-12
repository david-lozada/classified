<template>
	<q-btn
		@click="back"
      	round
      	color="dark"
      	size="md"
      	icon="arrow_left"
    />
</template>

<script>
export default {
  name: 'ButtonBack',
  methods: {
  	back() {
  		this.$router.go(-1)
  	}
  }
}
</script>