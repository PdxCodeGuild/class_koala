# Django and Vue

So you want to use Django as your backend, but you want more interactivity on your pages than you can provide with Django templates? Good news -- Django and Vue play very nicely together, and are easy to integrate. There's just a few things to keep in mind.

## Import Vue

To use Vue in a Django template, simply make sure the end of your `body` has a `script` tag to load Vue. I recommend writing your Vue app in a `script` tag at the bottom of your template instead of an external JavaScript file. This will make it easy to have your Django app pass data into your Vue app, like the CSRF token or even a context object.

```django
{% extends 'base.html' %}

{% block content %}

<div id="app">
  <p>{{ message }}</p> # Uh oh, this is the same template syntax as Django! We'll need to fix that...
</div>
<script src="https://unpkg.com/vue"></script>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      message: 'Hello world!',
    },
    methods: {
      logMessage: function () {
        console.log(this);
      }
    },
    mounted: function () {
      logMessage();
    }
  });
</script>

{% endblock %}
```

## Changing delimiters

By default, both Django and Vue templates use `{{ }}` to insert expressions. We need to change the delimiters that Vue uses to square brackets instead. This can be done by adding a `delimiters` value to our root Vue configuration object.

```django
{% extends 'base.html' %}

{% block content %}

<div id="app">
  <p>[[ message ]]</p> # Much better!
</div>
<script src="https://unpkg.com/vue"></script>
<script>
  let app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], // This is new
    data: {
      message: 'Hello world!',
    },
    methods: {
      logMessage: function () {
        console.log(this);
      }
    },
    mounted: function () {
      logMessage();
    }
  });
</script>

{% endblock %}
```

## Passing data context from Django to Vue

We now have a working Vue app in a Django template! How to we transfer over the data from our backend? We have two options:

  - Pass data from our Django view to our context and then load our template context into our Vue instance
  - If we have an API (this could be manually programmed Django views that return JSON or a full-fledged Django REST Framework app) we can use the `mounted` method on out root Vue component to fetch the data needed to initialize our page. To do this you need to build a REST API, but can then build a more modern and robust application.
  
Let's look at how to do both!

### Good -- Passing context to Javascript



### Better -- `mounted` API call

## Templates vs Vue

Vue and Dango templates fulfill the same role: presentation of data. With this in mind, decide which you are going to use to render your page. For instance, trying to use `{% for %}` and `v-for` in the same template will quickly make things complicated.
