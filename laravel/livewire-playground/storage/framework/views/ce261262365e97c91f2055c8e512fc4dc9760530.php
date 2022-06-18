<?php $__env->startSection('content'); ?>
    <?php
if (! isset($_instance)) {
    $html = \Livewire\Livewire::mount('auth.register')->html();
} elseif ($_instance->childHasBeenRendered('TnxUg1n')) {
    $componentId = $_instance->getRenderedChildComponentId('TnxUg1n');
    $componentTag = $_instance->getRenderedChildComponentTagName('TnxUg1n');
    $html = \Livewire\Livewire::dummyMount($componentId, $componentTag);
    $_instance->preserveRenderedChild('TnxUg1n');
} else {
    $response = \Livewire\Livewire::mount('auth.register');
    $html = $response->html();
    $_instance->logRenderedChild('TnxUg1n', $response->id(), \Livewire\Livewire::getRootElementTagName($html));
}
echo $html;
?>
<?php $__env->stopSection(); ?>
<?php echo $__env->make('layouts.app', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH /home/mark/workspace/study/development-lab/laravel/livewire-playground/resources/views/auth/register.blade.php ENDPATH**/ ?>