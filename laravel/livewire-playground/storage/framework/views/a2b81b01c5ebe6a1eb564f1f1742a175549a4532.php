<!doctype html>
<html class="h-full bg-gray-50">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Monofett&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="<?php echo e(asset('css/main.css')); ?>">
    <?php echo \Livewire\Livewire::styles(); ?>

</head>
<body class="h-full">
    <?php echo $__env->yieldContent('content'); ?>
    <?php echo \Livewire\Livewire::scripts(); ?>

</body>
</html>
<?php /**PATH /home/mark/workspace/study/development-lab/laravel/livewire-playground/resources/views/layouts/app.blade.php ENDPATH**/ ?>