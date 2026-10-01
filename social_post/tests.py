from django.test import TestCase
from django.urls import reverse
from user_auth.models import Users_data
from .models import Comment, Like, SocialPost


class SocialPostInteractionTests(TestCase):
	def setUp(self):
		self.user = Users_data.objects.create(name='Test User', email='test@example.com', password='test')
		self.post = SocialPost.objects.create(user=self.user, title='Test post', content='Post content')
		session = self.client.session
		session['user_id'] = self.user.id
		session.save()

	def test_like_action_toggles_like(self):
		url = reverse('social_post_like', args=[self.post.id])

		self.client.post(url)
		self.assertTrue(Like.objects.filter(post=self.post, user=self.user).exists())

		self.client.post(url)
		self.assertFalse(Like.objects.filter(post=self.post, user=self.user).exists())

	def test_comment_is_saved_and_rendered(self):
		self.client.post(
			reverse('social_post_comment', args=[self.post.id]),
			{'content': 'A useful comment'},
		)

		self.assertTrue(Comment.objects.filter(post=self.post, user=self.user, content='A useful comment').exists())
		response = self.client.get(reverse('social_post_list'))
		self.assertContains(response, 'A useful comment')

	def test_blank_comment_is_not_saved(self):
		self.client.post(
			reverse('social_post_comment', args=[self.post.id]),
			{'content': '   '},
		)

		self.assertFalse(Comment.objects.filter(post=self.post).exists())
