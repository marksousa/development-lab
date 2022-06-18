<?php
if (! isset($_instance)) {
    $html = \Livewire\Livewire::mount($name, $params)->html();
} elseif ($_instance->childHasBeenRendered('sZhWpGO')) {
    $componentId = $_instance->getRenderedChildComponentId('sZhWpGO');
    $componentTag = $_instance->getRenderedChildComponentTagName('sZhWpGO');
    $html = \Livewire\Livewire::dummyMount($componentId, $componentTag);
    $_instance->preserveRenderedChild('sZhWpGO');
} else {
    $response = \Livewire\Livewire::mount($name, $params);
    $html = $response->html();
    $_instance->logRenderedChild('sZhWpGO', $response->id(), \Livewire\Livewire::getRootElementTagName($html));
}
echo $html;
?>
<?php /**PATH /home/mark/workspace/study/development-lab/laravel/livewire-playground/vendor/livewire/livewire/src/Testing/../views/mount-component.blade.php ENDPATH**/ ?>