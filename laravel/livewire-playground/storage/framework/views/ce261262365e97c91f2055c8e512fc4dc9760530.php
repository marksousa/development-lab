<?php $__env->startSection('content'); ?>
    <?php
if (! isset($_instance)) {
    $html = \Livewire\Livewire::mount('auth.register')->html();
} elseif ($_instance->childHasBeenRendered('UI0qpwI')) {
    $componentId = $_instance->getRenderedChildComponentId('UI0qpwI');
    $componentTag = $_instance->getRenderedChildComponentTagName('UI0qpwI');
    $html = \Livewire\Livewire::dummyMount($componentId, $componentTag);
    $_instance->preserveRenderedChild('UI0qpwI');
} else {
    $response = \Livewire\Livewire::mount('auth.register');
    $html = $response->html();
    $_instance->logRenderedChild('UI0qpwI', $response->id(), \Livewire\Livewire::getRootElementTagName($html));
}
echo $html;
?>
<?php $__env->stopSection(); ?>
<?php echo $__env->make('layouts.app', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH /home/mark/workspace/study/development-lab/laravel/livewire-playground/resources/views/auth/register.blade.php ENDPATH**/ ?>